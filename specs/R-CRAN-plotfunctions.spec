%global packname  plotfunctions
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Various Functions to Facilitate Visualization of Data andAnalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
When analyzing data, plots are a helpful tool for visualizing data and
interpreting statistical models. This package provides a set of simple
tools for building plots incrementally, starting with an empty plot
region, and adding bars, data points, regression lines, error bars,
gradient legends, density distributions in the margins, and even pictures.
The package builds further on R graphics by simply combining functions and
settings in order to reduce the amount of code to produce for the user. As
a result, the package does not use formula input or special syntax, but
can be used in combination with default R plot functions. Note: Most of
the functions were part of the package 'itsadug', which is now split in
two packages: 1. the package 'itsadug', which contains the core functions
for visualizing and evaluating nonlinear regression models, and 2. the
package 'plotfunctions', which contains more general plot functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
