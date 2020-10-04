%global packname  prepdat
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          2%{?dist}%{?buildtag}
Summary:          Preparing Experimental Data for Statistical Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-psych >= 1.5.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-dplyr >= 0.4.2
Requires:         R-CRAN-psych >= 1.5.4
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-dplyr >= 0.4.2

%description
Prepares data for statistical analysis (e.g., analysis of variance ;ANOVA)
by enabling the user to easily and quickly merge (using the file_merge()
function) raw data files into one merged table and then aggregate the
merged table (using the prep() function) into a finalized table while
keeping track and summarizing every step of the preparation. The finalized
table contains several possibilities for dependent measures of the
dependent variable. Most suitable when measuring variables in an interval
or ratio scale (e.g., reaction-times) and/or discrete values such as
accuracy. Main functions included are file_merge() and prep(). The
file_merge() function vertically merges individual data files (in a long
format) in which each line is a single observation to one single dataset.
The prep() function aggregates the single dataset according to any
combination of grouping variables (i.e., between-subjects and
within-subjects independent variables, respectively), and returns a data
frame with a number of dependent measures for further analysis for each
cell according to the combination of provided grouping variables.
Dependent measures for each cell include among others means before and
after rejecting all values according to a flexible standard deviation
criteria, number of rejected values according to the flexible standard
deviation criteria, proportions of rejected values according to the
flexible standard deviation criteria, number of values before rejection,
means after rejecting values according to procedures described in Van
Selst & Jolicoeur (1994; suitable when measuring reaction-times), standard
deviations, medians, means according to any percentile (e.g., 0.05, 0.25,
0.75, 0.95) and harmonic means. The data frame prep() returns can also be
exported as a txt file to be used for statistical analysis in other
statistical programs.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
