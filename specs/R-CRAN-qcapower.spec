%global __brp_check_rpaths %{nil}
%global packname  qcapower
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Power and Required Sample Size in QCA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-devtools 
Requires:         R-stats 

%description
Researchers working with Qualitative Comparative Analysis (QCA) can use
the package to estimate power of a sufficient term using permutation
tests. A term can be anything: A condition, conjunction or disjunction of
any combination of these. The package further allows users to plot the
estimation results and to estimate the number of cases required to achieve
a certain level of power, given a prespecified null and alternative
hypothesis. Reference for the article introducing power estimation for QCA
is: Rohlfing, Ingo (2018) <doi:10.1017/pan.2017.30> (ungated version:
<doi:10.17605/OSF.IO/PC4DF>).

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
%{rlibdir}/%{packname}
