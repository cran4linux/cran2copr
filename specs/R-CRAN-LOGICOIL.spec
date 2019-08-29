%global packname  LOGICOIL
%global packver   0.99.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.0
Release:          1%{?dist}
Summary:          LOGICOIL: multi-state prediction of coiled-coil oligomericstate.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-nnet 
Requires:         R-nnet 

%description
This package contains the functions necessary to run the LOGICOIL
algorithm. LOGICOIL can be used to differentiate between antiparallel
dimers, parallel dimers, trimers and higher-order coiled-coil sequence. By
covering >90 percent of the known coiled-coil structures, LOGICOIL is a
net improvement compared with other existing methods, which achieve a
predictive coverage of around 31 percent of this population. As such,
LOGICOIL is particularly useful for researchers looking to characterize
novel coiled-coil sequences or studying coiled-coil containing protein
assemblies. It may also be used to assist in the structural
characterization of synthetic coiled-coil sequences.

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
