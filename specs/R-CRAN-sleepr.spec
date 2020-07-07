%global packname  sleepr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Analyse Activity and Sleep Behaviour

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-behavr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-behavr 
Requires:         R-CRAN-data.table 

%description
Use behavioural variables to score activity and infer sleep from bouts of
immobility. It is primarily designed to score sleep in fruit flies from
Drosophila Activity Monitor (TriKinetics) and Ethoscope data. It
implements sleep scoring using the "five-minute rule" (Hendricks et al.
(2000) <DOI:10.1016/S0896-6273(00)80877-6>), activity classification for
Ethoscopes (Geissmann et al. (2017) <DOI:10.1371/journal.pbio.2003026>)
and a new algorithm to detect when animals are dead.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
