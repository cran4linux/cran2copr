%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drugdevelopR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Utility-Based Optimal Phase II/III Drug Development Planning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-progressr 

%description
Plan optimal sample size allocation and go/no-go decision rules for phase
II/III drug development programs with time-to-event, binary or normally
distributed endpoints when assuming fixed treatment effects or a prior
distribution for the treatment effect, using methods from Kirchner et al.
(2016) <doi:10.1002/sim.6624> and Preussler (2020). Optimal is in the
sense of maximal expected utility, where the utility is a function taking
into account the expected cost and benefit of the program. It is possible
to extend to more complex settings with bias correction (Preussler S et
al. (2020) <doi:10.1186/s12874-020-01093-w>), multiple phase III trials
(Preussler et al. (2019) <doi:10.1002/bimj.201700241>), multi-arm trials
(Preussler et al. (2019) <doi:10.1080/19466315.2019.1702092>), and
multiple endpoints (Kieser et al. (2018) <doi:10.1002/pst.1861>).

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
