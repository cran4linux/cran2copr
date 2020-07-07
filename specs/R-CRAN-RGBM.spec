%global packname  RGBM
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}
Summary:          LS-TreeBoost and LAD-TreeBoost for Gene Regulatory NetworkReconstruction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doParallel 

%description
Provides an implementation of Regularized LS-TreeBoost & LAD-TreeBoost
algorithm for Regulatory Network inference from any type of expression
data (Microarray/RNA-seq etc). See Mall et al (2017) <doi:10.1101/132670>.

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
%{rlibdir}/%{packname}/libs
