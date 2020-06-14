%global packname  granova
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Graphical Analysis of Variance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 2.0.21
Requires:         R-CRAN-car >= 2.0.21

%description
This small collection of functions provides what we call elemental
graphics for display of anova results. The term elemental derives from the
fact that each function is aimed at construction of graphical displays
that afford direct visualizations of data with respect to the fundamental
questions that drive the particular anova methods. The two main functions
are granova.1w (a graphic for one way anova) and granova.2w (a
corresponding graphic for two way anova). These functions were written to
display data for any number of groups, regardless of their sizes (however,
very large data sets or numbers of groups can be problematic). For these
two functions a specialized approach is used to construct data-based
contrast vectors for which anova data are displayed. The result is that
the graphics use straight lines, and when appropriate flat surfaces, to
facilitate clear interpretations while being faithful to the standard
effect tests in anova. The graphic results are complementary to standard
summary tables for these two basic kinds of analysis of variance;
numerical summary results of analyses are also provided as side effects.
Two additional functions are granova.ds (for comparing two dependent
samples), and granova.contr (which provides graphic displays for a priori
contrasts). All functions provide relevant numerical results to supplement
the graphic displays of anova data. The graphics based on these functions
should be especially helpful for learning how the methods have been
applied to answer the question(s) posed. This means they can be
particularly helpful for students and non-statistician analysts. But these
methods should be quite generally helpful for work-a-day applications of
all kinds, as they can help to identify outliers, clusters or patterns, as
well as highlight the role of non-linear transformations of data. In the
case of granova.1w and granova.ds especially, several arguments are
provided to facilitate flexibility in the construction of graphics that
accommodate diverse features of data, according to their corresponding
display requirements. See the help files for individual functions.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
