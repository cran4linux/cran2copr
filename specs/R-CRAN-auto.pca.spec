%global packname  auto.pca
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Automatic Variable Reduction Using Principal Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-plyr 

%description
PCA done by eigenvalue decomposition of a data correlation matrix, here it
automatically determines the number of factors by eigenvalue greater than
1 and it gives the uncorrelated variables based on the rotated component
scores, Such that in each principal component variable which has the high
variance are selected. It will be useful for non-statisticians in
selection of variables. For more information, see the
<http://www.ijcem.org/papers032013/ijcem_032013_06.pdf> web page.

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

%files
%{rlibdir}/%{packname}
