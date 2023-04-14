%global __brp_check_rpaths %{nil}
%global packname  granovaGG
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Graphical Analysis of Variance Using ggplot2

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-CRAN-gridExtra >= 0.9.1
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-CRAN-gridExtra >= 0.9.1
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 

%description
This collection of functions in 'granovaGG' provides what we call
elemental graphics for display of anova results. The term elemental
derives from the fact that each function is aimed at construction of
graphical displays that afford direct visualizations of data with respect
to the fundamental questions that drive the particular anova methods. This
package represents a modification of the original granova package; the key
change is to use 'ggplot2', Hadley Wickham's package based on Grammar of
Graphics concepts (due to Wilkinson). The main function is granovagg.1w()
(a graphic for one way ANOVA); two other functions (granovagg.ds() and
granovagg.contr()) are to construct graphics for dependent sample analyses
and contrast-based analyses respectively. (The function granova.2w(),
which entails dynamic displays of data, is not currently part of
'granovaGG'.) The 'granovaGG' functions are to display data for any number
of groups, regardless of their sizes (however, very large data sets or
numbers of groups can be problematic). For granovagg.1w() a specialized
approach is used to construct data-based contrast vectors for which anova
data are displayed. The result is that the graphics use a straight line to
facilitate clear interpretations while being faithful to the standard
effect test in anova. The graphic results are complementary to standard
summary tables; indeed, numerical summary statistics are provided as side
effects of the graphic constructions. granovagg.ds() and granovagg.contr()
provide graphic displays and numerical outputs for a dependent sample and
contrast-based analyses. The graphics based on these functions can be
especially helpful for learning how the respective methods work to answer
the basic question(s) that drive the analyses. This means they can be
particularly helpful for students and non-statistician analysts. But these
methods can be of assistance for work-a-day applications of many kinds, as
they can help to identify outliers, clusters or patterns, as well as
highlight the role of non-linear transformations of data. In the case of
granovagg.1w() and granovagg.ds() several arguments are provided to
facilitate flexibility in the construction of graphics that accommodate
diverse features of data, according to their corresponding display
requirements. See the help files for individual functions.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
