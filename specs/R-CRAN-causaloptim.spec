%global __brp_check_rpaths %{nil}
%global packname  causaloptim
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to Specify Causal Graphs and Compute Bounds on Causal Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rcdd 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rcdd 

%description
When causal quantities are not identifiable from the observed data, it
still may be possible to bound these quantities using the observed data.
We outline a class of problems for which the derivation of tight bounds is
always a linear programming problem and can therefore, at least
theoretically, be solved using a symbolic linear optimizer. We extend and
generalize the approach of Balke and Pearl (1994)
<doi:10.1016/B978-1-55860-332-5.50011-0> and we provide a user friendly
graphical interface for setting up such problems via directed acyclic
graphs (DAG), which only allow for problems within this class to be
depicted. The user can then define linear constraints to further refine
their assumptions to meet their specific problem, and then specify a
causal query using a text interface. The program converts this user
defined DAG, query, and constraints, and returns tight bounds. The bounds
can be converted to R functions to evaluate them for specific datasets,
and to latex code for publication. The methods and proofs of tightness and
validity of the bounds are described in a preprint by Sachs, Gabriel, and
Sjölander (2020)
<https://sachsmc.github.io/causaloptim/articles/CausalBoundsMethods.pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
