%global packname  ProcData
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Process Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-keras >= 2.2.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-keras >= 2.2.4
Requires:         R-CRAN-Rcpp >= 0.12.16

%description
General tools for exploratory process data analysis. Process data refers
to the data describing participants' problem solving processes in
computer-based assessments. It is often recorded in computer log files.
This package provides two action sequence generators and implements two
automatic feature extraction methods that compress the information stored
in process data, which often has a nonstandard format, into standard
numerical vectors. This package also provides recurrent neural network
based models that relate response processes with other binary or scale
variables of interest. The functions that involve training and evaluating
neural networks are wrappers of functions in 'keras'.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
