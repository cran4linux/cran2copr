%global packname  stepp
%global packver   3.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0.0
Release:          3%{?dist}
Summary:          Subpopulation Treatment Effect Pattern Plot (STEPP)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-survival 
BuildRequires:    R-splines 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-survival 
Requires:         R-splines 

%description
A method to explore the treatment-covariate interactions in survival or
generalized linear model (GLM) for continuous, binomial and count data
arising from two or more treatment arms of a clinical trial. A permutation
distribution approach to inference is implemented, based on permuting the
covariate values within each treatment group. Bonetti M, Gelber RD (2004)
<DOI:10.1093/biostatistics/5.3.465>. Marco Bonetti, David Zahrieh, Bernard
F. Cole, and Richard D. Gelber (2009) <doi:10.1002/sim.3524>. Ann A.
Lazar, Bernard F. Cole, Marco Bonetti, and Richard D. Gelber (2010)
<doi:10.1200/JCO.2009.27.9182>. Lazar AA,Bonetti M,Cole BF,Yip WK,Gelber
RD (2016) <doi:10.1177/1740774515609106>. Wai-Ki Yip,Marco Bonetti,Bernard
F Cole,William Barcella,Xin Victoria Wang,Ann Lazar,and Richard D Gelber
(2016) <doi:10.1177/1740774516643297>. Wang XV, Cole B, Bonetti M, Gelber
RD (2016) < doi:10.1002/sim.6958>. Wai-Ki Yip (2017,
ISBN:978-3-319-48846-2).

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
%{rlibdir}/%{packname}/libs
