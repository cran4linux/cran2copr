%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rrnni
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate with RNNI Tree Space

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
Requires:         R-methods 
Requires:         R-CRAN-ape 

%description
Calculate RNNI distance between and manipulate with ranked trees. RNNI
stands for Ranked Nearest Neighbour Interchange and is an extension of the
classical NNI space (space of trees created by the NNI moves) to ranked
trees, where internal nodes are ordered according to their heights
(usually assumed to be times). The RNNI distance takes the tree topology
into account, as standard NNI does, but also penalizes changes in the
order of internal nodes, i.e. changes in the order of times of
evolutionary events. For more information about the RNNI space see:
Gavryushkin et al. (2018) <doi:10.1007/s00285-017-1167-9>, Collienne &
Gavryushkin (2021) <doi:10.1007/s00285-021-01567-5>, Collienne et al.
(2021) <doi:10.1007/s00285-021-01685-0>, and Collienne (2021)
<http://hdl.handle.net/10523/12606>.

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
