%global packname  PeakSegJoint
%global packver   2018.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2018.10.3
Release:          2%{?dist}
Summary:          Joint Peak Detection in Several ChIP-Seq Samples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-PeakError 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-penaltyLearning 
Requires:         R-CRAN-PeakError 
Requires:         R-parallel 
Requires:         R-CRAN-penaltyLearning 

%description
Jointly segment several ChIP-seq samples to find the peaks which are the
same and different across samples. The fast approximate maximum Poisson
likelihood algorithm is described in "PeakSegJoint: fast supervised peak
detection via joint segmentation of multiple count data samples"
<arXiv:1506.01286> by TD Hocking and G Bourque.

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
