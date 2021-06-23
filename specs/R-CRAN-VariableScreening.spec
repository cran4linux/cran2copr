%global __brp_check_rpaths %{nil}
%global packname  VariableScreening
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          High-Dimensional Screening for Semiparametric LongitudinalRegression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-splines 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-energy 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-expm 
Requires:         R-splines 
Requires:         R-MASS 
Requires:         R-CRAN-energy 

%description
Implements variable screening techniques for ultra-high dimensional
regression settings.  Techniques for independent (iid) data,
varying-coefficient models, and longitudinal data are implemented. The
package currently contains three screen functions: screenIID(), screenLD()
and screenVCM(), and six methods for simulating dataset: simulateDCSIS(),
simulateLD, simulateMVSIS(), simulateMVSISNY(), simulateSIRS() and
simulateVCM(). The package is based on the work of Li-Ping ZHU, Lexin LI,
Runze LI, and Li-Xing ZHU (2011) <DOI:10.1198/jasa.2011.tm10563>, Runze
LI, Wei ZHONG, & Liping ZHU (2012) <DOI:10.1080/01621459.2012.695654>,
Jingyuan LIU, Runze LI, & Rongling WU (2014)
<DOI:10.1080/01621459.2013.850086> Hengjian CUI, Runze LI, & Wei ZHONG
(2015) <DOI:10.1080/01621459.2014.920256>, and Wanghuan CHU, Runze LI and
Matthew REIMHERR (2016) <DOI:10.1214/16-AOAS912>. Special thanks are due
to Ling Zhang for providing detailed testing and proposing a method for
speed improvement on the simulation of data with AR-1 structure.

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
