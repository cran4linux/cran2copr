%global packname  pcnetmeta
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          3%{?dist}
Summary:          Patient-Centered Network Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Performs arm-based network meta-analysis for datasets with binary,
continuous, and count outcomes using the Bayesian methods of Zhang et al
(2014) <doi:10.1177/1740774513498322> and Lin et al (2017)
<doi:10.18637/jss.v080.i05>.

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
