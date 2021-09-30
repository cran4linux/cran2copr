%global __brp_check_rpaths %{nil}
%global packname  ReDirection
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Dominant Direction of Reactions of a Biochemical Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-gtools 

%description
Biologically relevant, yet mathematically sound constraints are used to
compute the propensity and thence infer the dominant direction of
reactions of a generic biochemical network. The reactions must be unique
and their number must exceed that of the reactants,i.e., reactions >=
reactants + 2. 'ReDirection', computes the null space of a user-defined
stoichiometry matrix. The spanning non-zero and unique reaction vectors
(RVs) are combinatorially summed to generate one or more subspaces
recursively. Every reaction is represented as a sequence of identical
components across all RVs of a particular subspace. The terms are
evaluated with (biologically relevant bounds, linear maps, tests of
convergence, descriptive statistics, vector norms) and the terms are
classified into forward-, reverse- and equivalent-subsets. Since, these
are mutually exclusive the probability of occurrence is binary (all, 1;
none, 0). The combined propensity of a reaction is the p1-norm of the
sub-propensities, i.e., sum of the products of the probability and maximum
numeric value of a subset (least upper bound, greatest lower bound). This,
if strictly positive is the probable rate constant, is used to infer
dominant direction and annotate a reaction as "Forward (f)", "Reverse (b)"
or "Equivalent (e)". The inherent computational complexity (NP-hard) per
iteration suggests that a suitable value for the number of reactions is
around 20. Three functions comprise ReDirection. These are check_matrix()
and reaction_vector() which are internal, and calculate_reaction_vector()
which is external.

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
