%global packname  Synth
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Synthetic Control Group Method for Comparative Case Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-optimx 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-optimx 

%description
Implements the synthetic control group method for comparative case studies
as described in Abadie and Gardeazabal (2003) and Abadie, Diamond, and
Hainmueller (2010, 2011, 2014). The synthetic control method allows for
effect estimation in settings where a single unit (a state, country, firm,
etc.) is exposed to an event or intervention. It provides a data-driven
procedure to construct synthetic control units based on a weighted
combination of comparison units that approximates the characteristics of
the unit that is exposed to the intervention. A combination of comparison
units often provides a better comparison for the unit exposed to the
intervention than any comparison unit alone.

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
%{rlibdir}/%{packname}/INDEX
