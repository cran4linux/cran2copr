%global packname  spc4sts
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}
Summary:          Statistical Process Control for Stochastic Textured Surfaces

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-LS2Wstat 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
Requires:         R-CRAN-LS2Wstat 
Requires:         R-rpart 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 

%description
Provides statistical process control tools for stochastic textured
surfaces. The current version supports the following tools: (1) generic
modeling of stochastic textured surfaces. (2) local defect monitoring and
diagnostics in stochastic textured surfaces, which was proposed by Bui and
Apley (2018a) <doi:10.1080/00401706.2017.1302362>. (3) global change
monitoring in the nature of stochastic textured surfaces, which was
proposed by Bui and Apley (2018b) <doi:10.1080/00224065.2018.1507559>. (4)
computation of dissimilarity matrix of stochastic textured surface images,
which was proposed by Bui and Apley (2019b)
<doi:10.1016/j.csda.2019.01.019>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
