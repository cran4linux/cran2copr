%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pwrFDR
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          FDR Power

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-TableMonster 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-TableMonster 

%description
Computing Average and TPX Power under various BHFDR type sequential
procedures. All of these procedures involve control of some summary of the
distribution of the FDP, e.g. the proportion of discoveries which are
false in a given experiment. The most widely known of these, the BH-FDR
procedure, controls the FDR which is the mean of the FDP. A lesser known
procedure, due to Lehmann and Romano, controls the FDX, or probability
that the FDP exceeds a user provided threshold. This is less conservative
than FWE control procedures but much more conservative than the BH-FDR
proceudre. This package and the references supporting it introduce a new
procedure for controlling the FDX which we call the BH-FDX procedure. This
procedure iteratively identifies, given alpha and lower threshold delta,
an alpha* less than alpha at which BH-FDR guarantees FDX control.  This
uses asymptotic approximation and is only slightly more conservative than
the BH-FDR procedure. Likewise, we can think of the power in multiple
testing experiments in terms of a summary of the distribution of the True
Positive Proportion (TPP), the portion of tests truly non-null distributed
that are called significant. The package will compute power, sample size
or any other missing parameter required for power defined as (i) the mean
of the TPP (average power) or (ii) the probability that the TPP exceeds a
given value, lambda, (TPX power) via asymptotic approximation. All
supplied theoretical results are also obtainable via simulation. The
suggested approach is to narrow in on a design via the theoretical
approaches and then make final adjustments/verify the results by
simulation. The theoretical results are described in Izmirlian, G (2020)
Statistics and Probability letters, "<doi:10.1016/j.spl.2020.108713>", and
an applied paper describing the methodology with a simulation study is in
preparation. See citation("pwrFDR").

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
