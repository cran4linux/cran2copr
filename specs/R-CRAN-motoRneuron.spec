%global __brp_check_rpaths %{nil}
%global packname  motoRneuron
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analyzing Paired Neuron Discharge Times for Time-DomainSynchronization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-methods 
Requires:         R-stats >= 3.4.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dygraphs 
Requires:         R-methods 

%description
The temporal relationship between motor neurons can offer explanations for
neural strategies. We combined functions to reduce neuron action potential
discharge data and analyze it for short-term, time-domain synchronization.
Even more so, motoRneuron combines most available methods for the
determining cross correlation histogram peaks and most available indices
for calculating synchronization into simple functions. See Nordstrom,
Fuglevand, and Enoka (1992) <doi:10.1113/jphysiol.1992.sp019244> for a
more thorough introduction.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
