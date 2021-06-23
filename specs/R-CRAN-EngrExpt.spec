%global __brp_check_rpaths %{nil}
%global packname  EngrExpt
%global packver   0.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Data sets from "Introductory Statistics for EngineeringExperimentation"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-lattice 
Requires:         R-lattice 

%description
Datasets from Nelson, Coffin and Copeland "Introductory Statistics for
Engineering Experimentation" (Elsevier, 2003) with sample code.

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
%{rlibdir}/%{packname}/dataplots.pdf
%{rlibdir}/%{packname}/dataplots.R
%{rlibdir}/%{packname}/dataplots.Rout
%doc %{rlibdir}/%{packname}/extract.R
%doc %{rlibdir}/%{packname}/TXT.zip
%{rlibdir}/%{packname}/INDEX
