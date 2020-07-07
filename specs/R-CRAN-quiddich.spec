%global packname  quiddich
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          QUick IDentification of DIagnostic CHaracters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 0.12.0
Requires:         R-core >= 0.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.2
Requires:         R-CRAN-ape >= 5.2

%description
Provides tools for an automated identification of diagnostic molecular
characters, i.e. such columns in a given nucleotide or amino acid
alignment that allow to distinguish taxa from each other. These characters
can then be used to complement the formal descriptions of the taxa, which
are often based on morphological and anatomical features. Especially for
morphologically cryptic species, this will be helpful. QUIDDICH
distinguishes between four different types of diagnostic characters. For
more information, see "Kuehn, A.L., Haase, M. 2019. QUIDDICH: QUick
IDentification of DIagnostic CHaracters."

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
%doc %{rlibdir}/%{packname}/extData
%{rlibdir}/%{packname}/INDEX
