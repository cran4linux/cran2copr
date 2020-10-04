%global packname  clustcurv
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Determining Groups in Multiples Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-npregfast 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-Gmedian 
Requires:         R-survival 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-npregfast 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-KernSmooth 
Requires:         R-CRAN-data.table 

%description
A method for determining groups in multiple curves with an automatic
selection of their number based on k-means or k-medians algorithms. The
selection of the optimal number is provided by bootstrap methods. The
methodology can be applied both in regression and survival framework.
Implemented methods are: Grouping multiple survival curves described by
Villanueva et al. (2018) <doi:10.1002/sim.8016>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
