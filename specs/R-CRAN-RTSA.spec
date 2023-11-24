%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RTSA
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Trial Sequential Analysis' for Error Control and Inference in Sequential Meta-Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Frequentist sequential meta-analysis based on 'Trial Sequential Analysis'
(TSA) in programmed in Java by the Copenhagen Trial Unit (CTU). The
primary function is the calculation of group sequential designs for
meta-analysis to be used for planning and analysis of both prospective and
retrospective sequential meta-analyses to preserve type-I-error control
under sequential testing. 'RTSA' includes tools for sample size and trial
size calculation for meta-analysis and core meta-analyses methods such as
fixed-effect and random-effects models and forest plots. TSA is described
in Wetterslev et. al (2008) <doi:10.1016/j.jclinepi.2007.03.013>. The
methods for deriving the group sequential designs are based on Jennison
and Turnbull (1999, ISBN:9780849303166).

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
