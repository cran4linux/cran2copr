%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PBtDesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Balanced t-Designs (PBtDesigns)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
The t-designs represent a generalized class of balanced incomplete block
designs in which the number of blocks in which any t-tuple of treatments
(t >= 2) occur together is a constant. When the focus of an experiment
lies in grading and selecting treatment subgroups, t-designs would be
preferred over the conventional ones, as they have the additional
advantage of t-tuple balance. t-designs can be advantageously used in
identifying the best crop-livestock combination for a particular location
in Integrated Farming Systems that will help in generating maximum profit.
But as the number of components increases, the number of possible
t-component combinations will also increase. Most often, combinations
derived from specific components are only practically feasible, for
example, in a specific locality, farmers may not be interested in keeping
a pig or goat and hence combinations involving these may not be of any use
in that locality. In such situations partially balanced t-designs with few
selected combinations appearing in a constant number of blocks (while
others not at all appearing) may be useful (Sayantani Karmakar, Cini
Varghese, Seema Jaggi & Mohd Harun
(2021)<doi:10.1080/03610918.2021.2008436>). Further, every location may
not have the resources to form equally sized homogeneous blocks. Partially
balanced t-designs with unequal block sizes (Damaraju Raghavarao & Bei
Zhou (1998)<doi:10.1080/03610929808832657>. Sayantani Karmakar, Cini
Varghese, Seema Jaggi & Mohd Harun (2022)." Partially Balanced t-designs
with unequal block sizes") prove to be more suitable for such
situations.This package generates three series of partially balanced
t-designs namely Series 1, Series 2 and Series 3. Series 1 and Series 2
are designs having equal block sizes and with treatment structures 4(t +
1) and a prime number, respectively. Series 3 consists of designs with
unequal block sizes and with treatment structure n(n-1)/2. This package is
based on the function named PBtD() for generating partially balanced
t-designs along with their parameters, information matrices, average
variance factors and canonical efficiency factors.

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
