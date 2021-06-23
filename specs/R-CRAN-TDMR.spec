%global __brp_check_rpaths %{nil}
%global packname  TDMR
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Tuned Data Mining in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SPOT >= 2.0
BuildRequires:    R-CRAN-twiddler 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-adabag 
Requires:         R-CRAN-SPOT >= 2.0
Requires:         R-CRAN-twiddler 
Requires:         R-CRAN-testit 
Requires:         R-methods 
Requires:         R-CRAN-adabag 

%description
Tuned Data Mining in R ('TDMR') performs the complete tuning of a data
mining task (predictive analytics, that is classification and regression).
Preprocessing parameters and modeling parameters can be tuned
simultaneously. It incorporates a variety of tuners (among them 'SPOT' and
'CMA' with package 'rCMA') and allows integration of additional tuners.
Noise handling in the data mining optimization process is supported, see
Koch et al. (2015) <doi:10.1016/j.asoc.2015.01.005>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/demo01cpu
%doc %{rlibdir}/%{packname}/demo02sonar
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tdmMapDesign.csv
%{rlibdir}/%{packname}/INDEX
