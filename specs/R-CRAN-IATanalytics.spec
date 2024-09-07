%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IATanalytics
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Effect Sizes and Reliability for Implicit Association Test (IAT) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Quickly score raw data outputted from an Implicit Association Test (IAT;
Greenwald, McGhee, & Schwartz, 1998) <doi:10.1037/0022-3514.74.6.1464>.
IAT scores are calculated as specified by Greenwald, Nosek, and Banaji
(2003) <doi:10.1037/0022-3514.85.2.197>.  The output of this function is a
data frame that consists of four rows containing the following
information: (1) the overall IAT effect size for the participant's
dataset, (2) the effect size calculated for odd trials only, (3) the
effect size calculated for even trials only, and (4) the proportion of
trials with reaction times under 300ms (which is important for exclusion
purposes). Items (2) and (3) allow for a measure of the internal
consistency of the IAT. Specifically, you can use the subsetted IAT effect
sizes for odd and even trials to calculate Cronbach's alpha across
participants in the sample.  The input function consists of three
arguments. First, indicate the name of the dataset to be analyzed. This is
the only required input. Second, indicate the number of trials in your
entire IAT (the default is set to 220, which is typical for most IATs).
Last, indicate whether congruent trials (e.g., flowers and pleasant) or
incongruent trials (e.g., guns and pleasant) were presented first for this
participant (the default is set to congruent).  Data files should consist
of six columns organized in order as follows: Block (0-6), trial (0-19 for
training blocks, 0-39 for test blocks), category (dependent on your IAT),
the type of item within that category (dependent on your IAT), a dummy
variable indicating whether the participant was correct or incorrect on
that trial (0=correct, 1=incorrect), and the participant’s reaction time
(in milliseconds).  A sample dataset (titled 'sampledata') is included in
this package to practice with.

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
