%global packname  LipidMS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Lipid Annotation for LC-MS/MS DIA Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-enviPick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-CHNOSZ 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-LipidMSdata 
Requires:         R-CRAN-enviPick 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-CHNOSZ 
Requires:         R-stats 
Requires:         R-CRAN-LipidMSdata 

%description
Lipid annotation in untargeted liquid chromatography-data independent
acquisition-mass spectrometry lipidomics based on fragmentation and
intensity rules. Alcoriza-Balaguer MI, Garcia-Canaveras JC, Lopez A, Conde
I, Juan O, Carretero J, Lahoz A (2019) <doi:10.1021/acs.analchem.8b03409>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
