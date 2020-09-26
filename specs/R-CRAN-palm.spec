%global packname  palm
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Point Process Models via the Palm Likelihood

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-gsl 
Requires:         R-methods 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-R6 

%description
Functions to fit point process models using the Palm likelihood. First
proposed by Tanaka, Ogata, and Stoyan (2008) <DOI:10.1002/bimj.200610339>,
maximisation of the Palm likelihood can provide computationally efficient
parameter estimation for point process models in situations where the full
likelihood is intractable. This package is chiefly focused on Neyman-Scott
point processes, but can also fit the void processes proposed by
Jones-Todd et al. (2019) <DOI:10.1002/sim.8046>. The development of this
package was motivated by the analysis of capture-recapture surveys on
which individuals cannot be identified---the data from which can
conceptually be seen as a clustered point process (Stevenson, Borchers,
and Fewster, 2019 <DOI:10.1111/biom.12983>). As such, some of the
functions in this package are specifically for the estimation of cetacean
density from two-camera aerial surveys.

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
