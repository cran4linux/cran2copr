%global packname  Rwave
%global packver   2.4-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.8
Release:          3%{?dist}%{?buildtag}
Summary:          Time-Frequency Analysis of 1-D Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14

%description
A set of R functions which provide an environment for the Time-Frequency
analysis of 1-D signals (and especially for the wavelet and Gabor
transforms of noisy signals). It was originally written for Splus by Rene
Carmona, Bruno Torresani, and Wen L. Hwang, first at the University of
California at Irvine and then at Princeton University.  Credit should also
be given to Andrea Wang whose functions on the dyadic wavelet transform
are included. Rwave is based on the book: "Practical Time-Frequency
Analysis: Gabor and Wavelet Transforms with an Implementation in S", by
Rene Carmona, Wen L. Hwang and Bruno Torresani (1998, eBook
ISBN:978008053942), Academic Press.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
