%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ResponseScan
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quick Screening of Response Patterns in Test and Survey Items

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-utils 

%description
One call screens the item responses of a test or questionnaire for
patterns that deserve a closer look before modelling: flat or long-string
responding, low intra-individual variability, multivariate outliers,
incoherent psychometric synonyms or even-odd halves, overuse of the
midpoint or of the extremes, duplicated response vectors and identical
patterns that arrive in series of consecutive submissions. Indices follow
Curran (2016) <doi:10.1016/j.jesp.2015.07.006>; person fit in item
response theory (the standardized log-likelihood) is optional, and
cut-offs can be taken from a reference group. Results are returned per
person, with flags, frequency tables of response patterns and plots. Whole
batches of data (a second collection phase, one classroom) can be compared
with a reference group: the item correlation structure, with permutation
tests that leave out flat responders and match the response level, and the
Jennrich (1970) <doi:10.1080/01621459.1970.10481133> test; the similarity
of consecutive rows; and near-duplicate respondents. Flagged respondents
can be removed in one step and the same confirmatory or exploratory factor
model can be refitted with and without them.

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
