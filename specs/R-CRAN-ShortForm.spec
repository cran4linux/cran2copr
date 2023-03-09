%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ShortForm
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Short Form Creation

License:          LGPL (>= 2.0, < 3) | Mozilla Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.5.22
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-lavaan >= 0.5.22
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-doSNOW 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Performs automatic creation of short forms of scales with an ant colony
optimization algorithm and a Tabu search. As implemented in the package,
the ant colony algorithm randomly selects items to build a model of a
specified length, then updates the probability of item selection according
to the fit of the best model within each set of searches. The algorithm
continues until the same items are selected by multiple ants a given
number of times in a row. On the other hand, the Tabu search changes one
parameter at a time to be either free, constrained, or fixed while keeping
track of the changes made and putting changes that result in worse fit in
a "tabu" list so that the algorithm does not revisit them for some number
of searches. See Leite, Huang, & Marcoulides (2008)
<doi:10.1080/00273170802285743> for an applied example of the ant colony
algorithm, and Marcoulides & Falk (2018)
<doi:10.1080/10705511.2017.1409074> for an applied example of the Tabu
search.

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
