%global packname  NCA
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}
Summary:          Necessary Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-sfa 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-sfa 
Requires:         R-KernSmooth 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
Performs a Necessary Condition Analysis (NCA). (Dul, J. 2016. Necessary
Condition Analysis (NCA). ''Logic and Methodology of 'Necessary but not
Sufficient' causality." Organizational Research Methods 19(1), 10-52,
<http://journals.sagepub.com/doi/abs/10.1177/1094428115584005>). NCA
identifies necessary (but not sufficient) conditions in datasets, where x
causes (e.g. precedes) y. Instead of drawing a regression line ''through
the middle of the data'' in an xy-plot, NCA draws the ceiling line. The
ceiling line y = f(x) separates the area with observations from the area
without observations. (Nearly) all observations are below the ceiling
line: y <= f(x). The empty zone is in the upper left hand corner of the
xy-plot (with the convention that the x-axis is ''horizontal'' and the
y-axis is ''vertical'' and that values increase ''upwards'' and ''to the
right''). The ceiling line is a (piecewise) linear non-decreasing line: a
linear step function or a straight line. It indicates which level of x
(e.g. an effort or input) is necessary but not sufficient for a (desired)
level of y (e.g. good performance or output). A quick start guide for
using this package can be found here: <http://repub.eur.nl/pub/78323/> or
<https://ssrn.com/abstract=2624981>.

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
