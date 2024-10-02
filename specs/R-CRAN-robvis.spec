%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robvis
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize the Results of Risk-of-Bias (ROB) Assessments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 

%description
Helps users in quickly visualizing risk-of-bias assessments performed as
part of a systematic review. It allows users to create weighted bar-plots
of the distribution of risk-of-bias judgments within each bias domain, in
addition to traffic-light plots of the specific domain-level judgments for
each study. The resulting figures are of publication quality and are
formatted according the risk-of-bias assessment tool use to perform the
assessments. Currently, the supported tools are ROB2.0 (for randomized
controlled trials; Sterne et al (2019) <doi:10.1136/bmj.l4898>), ROBINS-I
(for non-randomised studies of interventions; Sterne et al (2016)
<doi:10.1136/bmj.i4919>), and QUADAS-2 (for diagnostic accuracy studies;
Whiting et al (2011) <doi:10.7326/0003-4819-155-8-201110180-00009>).

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
