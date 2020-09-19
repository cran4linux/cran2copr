%global packname  MAPITR
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          MArginal ePIstasis Test for Regions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-CompQuadForm 

%description
A genetic analysis tool and variance component model for identifying
marginal epistasis between pathways and the rest of the genome. 'MAPITR'
uses as input a matrix of genotypes, a vector of phenotypes, and a list of
pathways, and iteratively tests each pathway for epistasis between any
variants within the pathway versus any variants remaining in the rest of
the genome. 'MAPITR' returns results in the form of p-values for every
pathway indicating whether the null model of there being no epistatic
interactions between a pathway and the rest of the genome can be rejected.

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
