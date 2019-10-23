%global packname  mopa
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Species Distribution MOdeling with Pseudo-Absences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-PresenceAbsence 
BuildRequires:    R-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-dismo 
Requires:         R-rpart 
Requires:         R-CRAN-tree 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-PresenceAbsence 
Requires:         R-lattice 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-abind 

%description
Tools for transferable species distribution modeling and pseudo-absence
data generation allowing the straightforward design of relatively complex
experiments with multiple factors affecting the uncertainty (variability)
of SDM outputs (pseudo-absence sample, climate projection, modeling
algorithm, etc.), and the quantification of the contribution of different
factors to the final variability following the method described in Deque
el al. (2010) <doi:10.1007/s00382-011-1053-x>. Multiple methods for
pseudo-absence data generation can be applied, including the novel
Three-step method as described in Iturbide et al. (2015)
<doi:10.1016/j.ecolmodel.2015.05.018>. Additionally, a function for niche
overlap calculation is provided, considering the metrics described in
Warren et al. (2008) <10.1111/j.1558-5646.2008.00482.x> and in Pianka
(1973) <10.1146/annurev.es.04.110173.000413>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
