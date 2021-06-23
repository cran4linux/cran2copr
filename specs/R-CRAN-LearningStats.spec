%global __brp_check_rpaths %{nil}
%global packname  LearningStats
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Elemental Descriptive and Inferential Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readODS 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readODS 

%description
Provides tools to teach students elemental statistics. The main topics
covered are descriptive statistics, probability models (discrete and
continuous variables) and statistical inference (confidence intervals and
hypothesis tests). One of the main advantages of this package is that
allows the user to read quite a variety of types of data files with one
unique command. Moreover it includes shortcuts to simple but up-to-now not
in R descriptive features such a complete frequency table or an histogram
with the optimal number of intervals. Related to model distributions (both
discrete and continuous), the package allows the student to easy plot the
mass/density function, distribution function and quantile function just
detailing as input arguments the known population parameters. The
inference related tools are basically confidence interval and hypothesis
testing. Having defined independent commands for these two tools makes it
easier for the student to understand what the software is performing, and
it also helps the student to have a better knowledge on which specific
tool they need to use in each situation. Moreover, the hypothesis testing
commands provide not only the numeric result on the screen but also a very
intuitive graph (which includes the statistic distribution, the observed
value of the statistic, the rejection area and the p-value) that is very
useful for the student to visualise the process. The regression section
includes up to now, a simple linear model, with one single command the
student can obtain the numeric summary as well as the corresponding
diagram with the adjusted regression model and a legend with basic
information (formula of the adjusted model and R-squared).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
