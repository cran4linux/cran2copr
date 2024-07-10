%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dosearch
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Effect Identification from Multiple Incomplete Data Sources

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Identification of causal effects from arbitrary observational and
experimental probability distributions via do-calculus and standard
probability manipulations using a search-based algorithm by Tikka,
Hyttinen and Karvanen (2021) <doi:10.18637/jss.v099.i05>. Allows for the
presence of mechanisms related to selection bias (Bareinboim and Tian,
2015) <doi:10.1609/aaai.v29i1.9679>, transportability (Bareinboim and
Pearl, 2014) <http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf>, missing data
(Mohan, Pearl, and Tian, 2013)
<http://ftp.cs.ucla.edu/pub/stat_ser/r410.pdf>) and arbitrary combinations
of these. Also supports identification in the presence of context-specific
independence (CSI) relations through labeled directed acyclic graphs
(LDAG). For details on CSIs see (Corander et al., 2019)
<doi:10.1016/j.apal.2019.04.004>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
