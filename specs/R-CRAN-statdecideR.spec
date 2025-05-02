%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statdecideR
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Statistical Analysis and Plotting with CLD

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-stringr 
Requires:         R-stats 

%description
A lightweight tool that provides a reproducible workflow for selecting and
executing appropriate statistical analysis in one-way or two-way
experimental designs. The package automatically checks for data normality,
conducts parametric (ANOVA) or non-parametric (Kruskal-Wallis) tests,
performs post-hoc comparisons with Compact Letter Displays (CLD), and
generates publication-ready boxplots, faceted plots, and heatmaps. It is
designed for researchers seeking fast, automated statistical summaries and
visualization. Based on established statistical methods including Shapiro
and Wilk (1965) <doi:10.2307/2333709>, Kruskal and Wallis (1952)
<doi:10.1080/01621459.1952.10483441>, Tukey (1949) <doi:10.2307/3001913>,
Fisher (1925) <ISBN:0050021702>, and Wickham (2016)
<ISBN:978-3-319-24277-4>.

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
