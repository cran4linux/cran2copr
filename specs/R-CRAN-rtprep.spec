%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtprep
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Screening, Trimming, and Aggregating Response Time Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A uniform interface to common response time preprocessing decisions that
precede analysing aggregated response times or fitting an evidence
accumulation model. Screening rules from different preprocessing routines
-- absolute cutoffs, standard deviation and median absolute deviation
criteria, recursive moving criteria, and model-based mixture flagging --
all return the same per-trial object, so that consequences of a
preprocessing choice can be compared rather than assumed. The package also
provides aggregation into EZ-diffusion summary statistics, diagnostics
reporting what each rule removed and where rules disagree. Finally,
generators for response time data with contaminants of known type are
provided, so that a chosen pipeline can be tested against ground truth.
Screening criteria follow Van Selst and Jolicoeur (1994)
<doi:10.1080/14640749408401131>, the contaminant mixture Ratcliff and
Tuerlinckx (2002) <doi:10.3758/BF03196302>, and the EZ-diffusion equations
Wagenmakers, van der Maas and Grasman (2007) <doi:10.3758/BF03194023>.

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
