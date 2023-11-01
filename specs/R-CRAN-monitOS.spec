%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  monitOS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Monitoring Overall Survival in Pivotal Trials in Indolent Cancers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 

%description
These guidelines are meant to provide a pragmatic, yet rigorous, help to
drug developers and decision makers, since they are shaped by three
fundamental ingredients: the clinically determined margin of detriment on
OS that is unacceptably high (delta null); the benefit on OS that is
plausible given the mechanism of action of the novel intervention (delta
alt); and the quantity of information (i.e. survival events) it is
feasible to accrue given the clinical and drug development setting. The
proposed guidelines facilitate transparent discussions between
stakeholders focusing on the risks of erroneous decisions and what might
be an acceptable trade-off between power and the false positive error
rate.

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
