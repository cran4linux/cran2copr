%global __brp_check_rpaths %{nil}
%global packname  QuantNorm
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Mitigating the Adverse Impact of Batch Effects in Sample PatternDetection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Modifies the distance matrix obtained from data with batch effects, so as
to improve the performance of sample pattern detection, such as
clustering, dimension reduction, and construction of networks between
subjects. The method has been published in Bioinformatics (Fei et al,
2018, <doi:10.1093/bioinformatics/bty117>). Also available on 'GitHub'
<https://github.com/tengfei-emory/QuantNorm>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
