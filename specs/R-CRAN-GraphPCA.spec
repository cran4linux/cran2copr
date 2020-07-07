%global packname  GraphPCA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Graphical Tools of Histogram PCA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggplot2movies 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggplot2movies 

%description
Histogram principal components analysis is the generalization of the PCA.
Histogram data are adapted to design complex and big data which histograms
used as variables (big data adapter). Functions implemented provides
numerical and graphical tools of an extension of PCA. Sun Makosso Kallyth
(2016) <doi:10.1002/sam.11270>. Sun Makosso Kallyth and Edwin Diday (2012)
<doi:10.1007/s11634-012-0108-0>.

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
