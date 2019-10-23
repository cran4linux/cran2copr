%global packname  DAC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Calculating Data Agreement Criterion Scores to Rank ExpertsBased on Their Beliefs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-blavaan 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-truncnorm 

%description
Allows to calculate Data Agreement Criterion (DAC) scores. This can be
done to determine prior-data conflict or to evaluate and compare multiple
priors, which can be experts' predictions. Bousquet (2008)
<doi.org/10.1080/02664760802192981>.

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
