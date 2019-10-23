%global packname  PeakSegDP
%global packver   2017.08.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2017.08.15
Release:          1%{?dist}
Summary:          Dynamic Programming Algorithm for Peak Detection in ChIP-SeqData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
A quadratic time dynamic programming algorithm can be used to compute an
approximate solution to the problem of finding the most likely
changepoints with respect to the Poisson likelihood, subject to a
constraint on the number of segments, and the changes which must
alternate: up, down, up, down, etc. For more info read
<http://proceedings.mlr.press/v37/hocking15.html> "PeakSeg: constrained
optimal segmentation and supervised penalty learning for peak detection in
count data" by TD Hocking et al, proceedings of ICML2015.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
