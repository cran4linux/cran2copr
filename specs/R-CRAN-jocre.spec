%global packname  jocre
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Joint Confidence Regions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-TSP 
Requires:         R-boot 
Requires:         R-KernSmooth 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-TSP 

%description
Computing and plotting joint confidence regions and intervals. Regions
include classical ellipsoids, minimum-volume or minimum-length regions,
and an empirical Bayes region. Intervals include the TOST procedure with
ordinary or expanded intervals and a fixed-sequence procedure. Such
regions and intervals are useful e.g., for the assessment of
multi-parameter (bio-)equivalence. Joint confidence regions for the mean
and variance of a normal distribution are available as well.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
