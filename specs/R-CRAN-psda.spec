%global __brp_check_rpaths %{nil}
%global packname  psda
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Polygonal Symbolic Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-stats 

%description
A toolbox in symbolic data framework as a statistical learning and data
mining solution for symbolic polygonal data analysis. This study is a new
approach in data analysis and it was proposed by Silva et al. (2019)
<doi:10.1016/j.knosys.2018.08.009>. The package presents the estimation of
main descriptive statistical measures, e.g, mean, covariance, variance,
correlation and coefficient of variation. In addition, a method to obtain
polygonal data from classical data is presented. Empirical probability
distribution function based on symbolic polygonal histogram and a
regression model with its main measures are presented.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
