%global packname  sparseFLMM
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Linear Mixed Models for Irregularly or Sparsely Sampled Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8.12
BuildRequires:    R-CRAN-refund >= 0.1.22
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-data.table 
Requires:         R-mgcv >= 1.8.12
Requires:         R-CRAN-refund >= 0.1.22
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-data.table 

%description
Estimation of functional linear mixed models for irregularly or sparsely
sampled data based on functional principal component analysis.

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
