%global packname  AcousticNDLCodeR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Coding Sound Files for Use with NDL

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-seewave 
Requires:         R-parallel 

%description
Make acoustic cues to use with the R packages 'ndl' or 'ndl2'. The package
implements functions used in the PLoS ONE paper: Denis Arnold, Fabian
Tomaschek, Konstantin Sering, Florence Lopez, and R. Harald Baayen (2017).
Words from spontaneous conversational speech can be recognized with
human-like accuracy by an error-driven learning algorithm that
discriminates between meanings straight from smart acoustic features,
bypassing the phoneme as recognition unit.  PLoS ONE 12(4):e0174623
<doi:10.1371/journal.pone.0174623> More details can be found in the paper
and the supplement. 'ndl' is available on CRAN. 'ndl2' is available by
request from <konstantin.sering@uni-tuebingen.de>.

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
