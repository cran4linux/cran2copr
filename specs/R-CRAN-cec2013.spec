%global packname  cec2013
%global packver   0.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Benchmark functions for the Special Session and Competition onReal-Parameter Single Objective Optimization at CEC-2013

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0

%description
This package provides R wrappers for the C implementation of 28 benchmark
functions defined for the Special Session and Competition on
Real-Parameter Single Objective Optimization at CEC-2013. The focus of
this package is to provide an open-source and multi-platform
implementation of the CEC2013 benchmark functions, in order to make easier
for researchers to test the performance of new optimization algorithms in
a reproducible way. The original C code (Windows only) was provided by
Jane Jing Liang, while GNU/Linux comments were made by Janez Brest. This
package was gently authorised for publication on CRAN by Ponnuthurai
Nagaratnam Suganthan. The official documentation is available at
http://www.ntu.edu.sg/home/EPNSugan/index_files/CEC2013/CEC2013.htm. Bugs
reports/comments/questions are very welcomed (in English, Spanish or
Italian).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
