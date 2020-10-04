%global packname  rescue
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Imputation for Single-Cell RNA-Seq Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-CRAN-reticulate >= 1.14
BuildRequires:    R-CRAN-dbscan >= 1.1.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-CRAN-reticulate >= 1.14
Requires:         R-CRAN-dbscan >= 1.1.3
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-irlba 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 

%description
Given a log-transformed expression matrix and list of informative genes:
subsample informative genes, cluster samples using shared nearest
neighbors clustering, estimate missing expression values with the
distribution mean of means extrapolated from these cell clusterings, and
return an imputed expression matrix. See Tracy, S., Yuan, G.C. and Dries,
R. (2019) <doi:10.1186/s12859-019-2977-0> for more details.

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
