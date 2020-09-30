%global packname  rMIDAS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation using Denoising Autoencoders

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mltools 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mltools 
Requires:         R-CRAN-reticulate 

%description
A tool that allows users to impute missing data with 'MIDAS', a multiple
imputation method using denoising autoencoders as documented in Lall and
Robinson (2020) <doi:10.33774/apsa-2020-3tk40-v3>. This method has
significant accuracy and efficiency advantages over other multiple
imputation strategies, particularly when run on large datasets with many
columns or categories. Alongside interfacing with 'Python' to run the core
algorithm, this package contains tools to process the data before and
after model training, run imputation model diagnostics, generate multiple
completed datasets, and estimate multiply-imputed regression models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
