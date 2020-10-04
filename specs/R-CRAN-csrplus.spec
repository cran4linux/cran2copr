%global packname  csrplus
%global packver   1.03-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.03.0
Release:          3%{?dist}%{?buildtag}
Summary:          Methods to Test Hypotheses on the Distribution of Spatial PointProcesses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-sp 

%description
Includes two functions to evaluate the hypothesis of complete spatial
randomness (csr) in point processes.  The function 'mwin' calculates
quadrat counts to estimate the intensity of a spatial point process
through the moving window approach proposed by Bailey and Gatrell (1995).
Event counts are computed within a window of a set size over a fine
lattice of points within the region of observation.  The function 'pielou'
uses the nearest neighbor test statistic and asymptotic distribution
proposed by Pielou (1959) to compare the observed point process to one
generated under csr.  The value can be compared to that given by the more
widely used test proposed by Clark and Evans (1954).

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
